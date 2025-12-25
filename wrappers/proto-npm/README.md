# @chaty/proto

TypeScript Protobuf bindings for Chaty services.

Includes message definitions and gRPC client/server stubs for both Node.js and web browsers.

## Installation

```bash
npm install @chaty/proto
# or
pnpm add @chaty/proto
```

## Usage

### Node.js (gRPC-JS)

```typescript
import { UsersClient } from '@chaty/proto/users/v1';
import { createChannel } from '@grpc/grpc-js';

const channel = createChannel('localhost:50051');
const client = new UsersClient(channel);
```

### Browser (gRPC-Web)

```typescript
import { UsersClient } from '@chaty/proto/web/users/v1';

const client = new UsersClient({
  host: 'http://localhost:8080'
});
```

## Exports

- `./users/v1` - Users service messages and client
- `./shared/v1` - Shared message definitions
- `./web/users/v1` - Browser-compatible gRPC-Web client for users
- `./web/shared/v1` - Browser-compatible shared definitions
