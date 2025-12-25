# @chaty-app/proto

TypeScript Protobuf bindings for Chaty services.

Includes message definitions and gRPC client/server stubs for both Node.js and web browsers.

## Installation

```bash
npm install @chaty-app/proto
# or
pnpm add @chaty-app/proto
```

## Usage

### Node.js (gRPC-JS)

```typescript
import { ChatyServiceClient } from '@chaty-app/proto/service/v1';
import { createChannel } from '@grpc/grpc-js';

const channel = createChannel('localhost:50051');
const client = new ChatyServiceClient(channel);

// Call UsersLogin RPC
const response = await client.usersLogin({
  email: 'user@example.com',
  password: 'password123'
});
```

### Browser (gRPC-Web)

```typescript
import { ChatyServiceClient } from '@chaty-app/proto/web/service/v1';

const client = new ChatyServiceClient({
  host: 'http://localhost:8080'
});

// Call UsersLogin RPC
const response = await client.usersLogin({
  email: 'user@example.com',
  password: 'password123'
});
```

## Exports

- `./service/v1` - Chaty unified service (authentication, user management)
- `./shared/v1` - Shared message definitions
- `./web/service/v1` - Browser-compatible gRPC-Web for Chaty service
- `./web/shared/v1` - Browser-compatible shared definitions
