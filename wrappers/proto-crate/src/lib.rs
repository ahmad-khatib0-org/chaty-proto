#![allow(clippy::all)]

pub mod shared {
  pub mod v1 {
    include!("shared.v1.rs");
  }
}

pub mod service {
  pub mod v1 {
    include!("service.v1.rs");
  }
}

// Re-export main types at crate root
pub use shared::v1::*;
pub use service::v1::*;
