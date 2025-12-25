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
        "users/v1/users.proto",
        "users/v1/auth.proto",
      ],
      &["."],
    )?;

  Ok(())
}
