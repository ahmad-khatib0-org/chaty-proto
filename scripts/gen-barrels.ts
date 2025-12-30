import fs from 'fs'
import path from 'path'

function toPascalCase(input: string): string {
  return input
    .replace(/[-_]([a-z])/g, (_, char) => char.toUpperCase())
    .replace(/^([a-z])/, (_, char) => char.toUpperCase())
}

function generateBarrels(rootDir: string) {
  if (!fs.existsSync(rootDir)) return

  function walk(dir: string) {
    const entries = fs.readdirSync(dir, { withFileTypes: true })
    const files = entries.filter((e) => e.isFile() && e.name.endsWith('.ts') && e.name !== 'index.ts')
    const dirs = entries.filter((e) => e.isDirectory())

    if (files.length > 0) {
      const content =
        files
          .map((f) => {
            const base = f.name.replace(/\.ts$/, '')
            const varName = toPascalCase(base.replace(/_pb$/, ''))
            // Important: .js extension for ESM compatibility in Next.js
            return `export * as ${varName} from './${base}.js';`
          })
          .join('\n') + '\n'

      fs.writeFileSync(path.join(dir, 'index.ts'), content)
      console.log(`✅ Created barrel: ${dir}/index.ts`)
    }

    dirs.forEach((d) => walk(path.join(dir, d.name)))
  }
  walk(rootDir)
}

generateBarrels('wrappers/proto-npm/src/node')
generateBarrels('wrappers/proto-npm/src/web')

// Root index remains empty
fs.writeFileSync('wrappers/proto-npm/src/index.ts', '// Root index\n')
