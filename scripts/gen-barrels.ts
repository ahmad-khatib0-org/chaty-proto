import fs from 'fs'
import path from 'path'

function toPascalCase(input: string): string {
  return input
    .replace(/[-_]([a-z])/g, (_, char) => char.toUpperCase())
    .replace(/^([a-z])/, (_, char) => char.toUpperCase())
}

function generateBarrels(rootDir: string) {
  function walk(dir: string) {
    const subdirs = fs.readdirSync(dir, { withFileTypes: true })

    const files: string[] = []
    const dirs: string[] = []

    for (const entry of subdirs) {
      if (entry.isDirectory()) {
        dirs.push(entry.name)
      } else if (
        entry.isFile() &&
        (entry.name.endsWith('.ts') || entry.name.endsWith('.js')) &&
        entry.name !== 'index.ts' &&
        !entry.name.endsWith('.d.ts')
      ) {
        files.push(entry.name)
      }
    }

    // Generate index for proto files in this directory
    if (files.length > 0) {
      const exportLines = files.map((file) => {
        const base = file.replace(/\.(ts|js)$/, '') // remove extension
        const varName = toPascalCase(base)
        return `import * as ${varName} from './${base}.js';`
      })

      const reexportNames = files.map((file) => {
        const base = file.replace(/\.(ts|js)$/, '')
        return toPascalCase(base)
      })

      const indexContent =
        exportLines.join('\n') + '\n\n' + `export {\n  ${reexportNames.join(',\n  ')}\n};\n`
      const indexPath = path.join(dir, 'index.ts')
      fs.writeFileSync(indexPath, indexContent)
      console.log(`Generated: ${indexPath}`)
    }

    // Generate index for subdirectories
    if (dirs.length > 0) {
      const exportLines = dirs.map((dirName) => {
        return `export * from './${dirName}/index.js';`
      })
      const indexContent = exportLines.join('\n') + '\n'
      const indexPath = path.join(dir, 'index.ts')
      
      // If we already have proto files, append subdirs; otherwise create new
      if (!files.length) {
        fs.writeFileSync(indexPath, indexContent)
        console.log(`Generated: ${indexPath}`)
      }
    }

    for (const subdir of dirs) {
      walk(path.join(dir, subdir))
    }
  }

  walk(rootDir)
}

generateBarrels('wrappers/proto-npm/src/node')
generateBarrels('wrappers/proto-npm/src/web')

// Generate root level index that exports node and web
function generateRootIndex() {
  const rootContent = `export * from './node/index.js';\n`
  const rootPath = 'wrappers/proto-npm/src/index.ts'
  fs.writeFileSync(rootPath, rootContent)
  console.log(`Generated: ${rootPath}`)
}
generateRootIndex()
