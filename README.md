# Chaty Proto

Protobuf definitions for Chaty services. Generates Rust crates and TypeScript packages for Node.js and web browsers.

## Structure

```
chaty-proto/
├── service/v1/            # Chaty unified service definition (RPC calls)
├── shared/v1/             # Shared message definitions
├── wrappers/
│   ├── proto-crate/       # Rust crate (@crates.io)
│   └── proto-npm/         # NPM package (@chaty/proto)
├── scripts/               # Code generation utilities
├── build.rs              # Rust build script (generates Rust code)
├── buf.gen.yaml          # Buf config (generates TypeScript)
└── Makefile              # Build automation
```

## Quick Start

### Generate Code

```bash
# Install dependencies
pnpm install

# Generate all (Rust + TypeScript)
make generate
```

### Publish Release

```bash
# Create and push version tag (updates all version files)
make release VERSION=0.1.1

# Publish to crates.io and npm.js
make publish
```

Alternatively, GitHub Actions auto-publishes when you push a `v*` tag.

## Packages

### Rust: `chaty-proto`

gRPC server stubs + message definitions via Tonic.

```bash
cd wrappers/proto-crate
cargo publish
```

### TypeScript: `@chaty-app/proto`

Dual exports:

- **Node.js**: gRPC-JS client/server
- **Browser**: gRPC-Web client

```bash
cd wrappers/proto-npm
npm publish --access public
```

## Dependencies

- `pnpm@10.10.0`
- `buf` CLI
- Rust toolchain (for Cargo)
- Node.js 16+

## Development

### Add new proto module

1. Create `module/v1/` directory with `.proto` files
2. Update `build.rs` to include new protos
3. Run `make generate`

### Watch mode

```bash
# Watch and rebuild TypeScript
cd wrappers/proto-npm && pnpm watch
```

## Scripts

- `scripts/build-cjs.js` - Converts ESM to CommonJS for Node.js
- `scripts/gen-barrels.ts` - Auto-generates barrel index files
- `Makefile` - Build automation (generate, release, publish)
