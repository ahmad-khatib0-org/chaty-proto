.PHONY: generate release clean publish

VERSION ?=
MSG ?=

# -----------------------------------------------------------------------------
# Generate all protobuf artifacts
# -----------------------------------------------------------------------------
generate:
	@echo "Cleaning previous generated code..."
	rm -rf wrappers/proto-npm/dist wrappers/proto-npm/src/node wrappers/proto-npm/src/web
	
	@echo "Generating protobuf files..."
	# Injected PATH ensures buf finds the plugins in root node_modules
	PATH="$(shell pwd)/node_modules/.bin:$(PATH)" buf generate 

	@echo "Generating TypeScript barrel files..."
	pnpm exec tsx scripts/gen-barrels.ts

	@echo "Compiling TypeScript (Pure ESM)..."
	pnpm --filter @chaty-app/proto exec tsc

	@echo "✅ Generation complete"
# -----------------------------------------------------------------------------
# Release: commit + tag + push
# -----------------------------------------------------------------------------
release:
ifeq ($(VERSION),)
	@echo "❌ ERROR: No version specified for release."
	@exit 1
endif

	@echo "📦 Updating versions to $(VERSION)..."
	sed -i.bak 's/^version = ".*"/version = "$(VERSION)"/' ./wrappers/proto-crate/Cargo.toml && rm -f wrappers/proto-crate/Cargo.toml.bak
	sed -i.bak 's/^\(\s*\)"version": ".*"/\1"version": "$(VERSION)"/' ./wrappers/proto-npm/package.json && rm -f wrappers/proto-npm/package.json.bak

	@echo "Generating updated Cargo.lock..."
	cargo check  # This will update Cargo.lock with the new version

	@echo "Waiting some seconds before commiting..."
	sleep 5

	@echo "Committing generated files and tagging release..."
	git add -A
	git commit -m "$${MSG:-chore(proto): generated artifacts for $(VERSION)}" || true

	# create annotated tag (skip if exists)
	if git rev-parse "refs/tags/v$(VERSION)" >/dev/null 2>&1; then \
	  echo "Tag v$(VERSION) already exists — updating commit (force)"; \
	  git tag -f -a "v$(VERSION)" -m "proto gen $(VERSION)"; \
	else \
	  git tag -a "v$(VERSION)" -m "proto gen $(VERSION)"; \
	fi
	git push origin --tags || true
	git push origin main
	@echo "✅ Release complete"

# -----------------------------------------------------------------------------
# Clean generated artifacts
# -----------------------------------------------------------------------------
clean:
	cd wrappers/proto-crate && cargo clean
