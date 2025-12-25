// Re-export all generated proto modules
pub mod shared {
    pub mod v1 {
        #![allow(clippy::derive_partial_eq_without_eq)]
        include!(concat!(env!("OUT_DIR"), "/shared.v1.rs"));
    }
}

pub mod users {
    pub mod v1 {
        #![allow(clippy::derive_partial_eq_without_eq)]
        include!(concat!(env!("OUT_DIR"), "/users.v1.rs"));
    }
}
