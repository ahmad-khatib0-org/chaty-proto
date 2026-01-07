fn main() -> Result<(), Box<dyn std::error::Error>> {
  let out_dir = "wrappers/proto-crate/src";
  std::fs::create_dir_all(out_dir)?;

  tonic_build::configure()
    .out_dir(out_dir)
    .build_server(true)
    .build_client(true)
    .type_attribute(".", "#[derive(serde::Serialize, serde::Deserialize)]")
    .file_descriptor_set_path(format!("{}/descriptor.bin", out_dir))
    .compile_protos(
      &[
        "shared/v1/error.proto",
        "shared/v1/files.proto",
        "shared/v1/struct.proto",
        "shared/v1/time.proto",
        "shared/v1/types.proto",
        "shared/v1/wrappers.proto",
        "service/v1/groups.proto",
        "service/v1/main.proto",
        "service/v1/messages.proto",
        "service/v1/messages_db.proto",
        "service/v1/users.proto",
        "service/v1/users_db.proto",
      ],
      &["."],
    )?;

  // Generate Envoy external_auth proto + minimal dependencies
  tonic_build::configure()
    .out_dir(format!("{}/envoy", out_dir))
    .build_server(true)
    .compile_well_known_types(true)
    .file_descriptor_set_path(format!("{}/envoy_descriptor.bin", out_dir))
    .compile_protos(
      &["envoy/service/auth/v3/external_auth.proto"], // path relative to include folder
      &[
        "third_party/proto/envoyproxy/api", // Envoy protos
        "third_party/proto/googleapis",
        "third_party/proto/udpa",
        "third_party/proto/validate",
      ],
    )?;

  Ok(())
}
