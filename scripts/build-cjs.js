// scripts/build-cjs.js
// Usage: node ./scripts/build-cjs.js <target-dist-root>
// Example: node ./scripts/build-cjs.js ./wrappers/proto-npm/dist
// If no arg provided, defaults to ./wrappers/proto-npm/dist

const fs = require('fs')
const path = require('path')
const { build } = require('esbuild')

async function main() {
  const repoRoot = process.cwd()
  const distArg = process.argv[2] || path.join('wrappers', 'proto-npm', 'dist')
  const distRoot = path.resolve(repoRoot, distArg)
  const srcNode = path.join(distRoot, 'node')
  const outNodeCjs = path.join(distRoot, 'node-cjs')

  if (!fs.existsSync(srcNode)) {
    console.error('Source directory not found:', srcNode)
    process.exit(1)
  }

  console.log(`Transforming ESM ${srcNode} -> CommonJS ${outNodeCjs}`)
  await transformDir(srcNode, outNodeCjs)
  console.log('CJS build complete')
}

async function transformDir(srcDir, outDir) {
  fs.mkdirSync(outDir, { recursive: true })
  const entries = fs.readdirSync(srcDir, { withFileTypes: true })

  for (const ent of entries) {
    const srcPath = path.join(srcDir, ent.name)
    const outPath = path.join(outDir, ent.name)

    if (ent.isDirectory()) {
      await transformDir(srcPath, outPath)
      continue
    }

    if (ent.isFile()) {
      if (srcPath.endsWith('.js')) {
        const relOut = outPath
        await build({
          entryPoints: [srcPath],
          outfile: relOut,
          platform: 'node',
          format: 'cjs',
          bundle: false,
          sourcemap: true,
          target: ['node16'],
          logLevel: 'silent',
        })
      } else if (srcPath.endsWith('.d.ts') || srcPath.endsWith('.map') || srcPath.endsWith('.json')) {
        fs.mkdirSync(path.dirname(outPath), { recursive: true })
        fs.copyFileSync(srcPath, outPath)
      } else {
        fs.mkdirSync(path.dirname(outPath), { recursive: true })
        fs.copyFileSync(srcPath, outPath)
      }
    }
  }
}

if (require.main === module) {
  main().catch((err) => {
    console.error(err)
    process.exit(1)
  })
}
