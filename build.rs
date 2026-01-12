fn main() -> Result<(), Box<dyn std::error::Error>> {
  let out_dir = "wrappers/proto-crate/src";
  std::fs::create_dir_all(out_dir)?;

  tonic_build::configure()
    .out_dir(out_dir)
    .build_server(true)
    .build_client(true)
    .type_attribute(".", "#[derive(serde::Serialize, serde::Deserialize)]")
    // NOTE: Scylla derives for simple types only (no Enum, no oneof, no HashMap, )
    .type_attribute(
      "service.v1.OverrideField",
      "#[derive(scylla::SerializeValue, scylla::DeserializeValue)]",
    )
    .type_attribute(
      "service.v1.Role",
      "#[derive(scylla::SerializeValue, scylla::DeserializeValue)]",
    )
    .type_attribute(
      "service.v1.ChannelGroup",
      "#[derive(scylla::SerializeValue, scylla::DeserializeValue)]",
    )
    .type_attribute(
      "service.v1.ChannelSavedMessages",
      "#[derive(scylla::SerializeValue, scylla::DeserializeValue)]",
    )
    .type_attribute(
      "service.v1.ChannelDirectMessage",
      "#[derive(scylla::SerializeValue, scylla::DeserializeValue)]",
    )
    .type_attribute(
      "service.v1.MessageWebhook",
      "#[derive(scylla::SerializeValue, scylla::DeserializeValue)]",
    )
    .type_attribute(
      "service.v1.MessageSystemText",
      "#[derive(scylla::SerializeValue, scylla::DeserializeValue)]",
    )
    .type_attribute(
      "service.v1.MessageSystemUserAdded",
      "#[derive(scylla::SerializeValue, scylla::DeserializeValue)]",
    )
    .type_attribute(
      "service.v1.MessageSystemUserRemove",
      "#[derive(scylla::SerializeValue, scylla::DeserializeValue)]",
    )
    .type_attribute(
      "service.v1.MessageSystemUserJoined",
      "#[derive(scylla::SerializeValue, scylla::DeserializeValue)]",
    )
    .type_attribute(
      "service.v1.MessageSystemUserLeft",
      "#[derive(scylla::SerializeValue, scylla::DeserializeValue)]",
    )
    .type_attribute(
      "service.v1.MessageSystemUserKicked",
      "#[derive(scylla::SerializeValue, scylla::DeserializeValue)]",
    )
    .type_attribute(
      "service.v1.MessageSystemUserBanned",
      "#[derive(scylla::SerializeValue, scylla::DeserializeValue)]",
    )
    .type_attribute(
      "service.v1.MessageSystemChannelRenamed",
      "#[derive(scylla::SerializeValue, scylla::DeserializeValue)]",
    )
    .type_attribute(
      "service.v1.MessageSystemChannelDescriptionChanged",
      "#[derive(scylla::SerializeValue, scylla::DeserializeValue)]",
    )
    .type_attribute(
      "service.v1.MessageSystemChannelIconChanged",
      "#[derive(scylla::SerializeValue, scylla::DeserializeValue)]",
    )
    .type_attribute(
      "service.v1.MessageSystemChannelOwnershipChanged",
      "#[derive(scylla::SerializeValue, scylla::DeserializeValue)]",
    )
    .type_attribute(
      "service.v1.MessageSystemMessagePinned",
      "#[derive(scylla::SerializeValue, scylla::DeserializeValue)]",
    )
    .type_attribute(
      "service.v1.MessageSystemMessageUnpinned",
      "#[derive(scylla::SerializeValue, scylla::DeserializeValue)]",
    )
    .type_attribute(
      "service.v1.MessageSystemCallStarted",
      "#[derive(scylla::SerializeValue, scylla::DeserializeValue)]",
    )
    .type_attribute(
      "service.v1.EmbedImage",
      "#[derive(scylla::SerializeValue, scylla::DeserializeValue)]",
    )
    .type_attribute(
      "service.v1.EmbedVideo",
      "#[derive(scylla::SerializeValue, scylla::DeserializeValue)]",
    )
    .type_attribute(
      "service.v1.EmbedYouTube",
      "#[derive(scylla::SerializeValue, scylla::DeserializeValue)]",
    )
    .type_attribute(
      "service.v1.EmbedLightspeed",
      "#[derive(scylla::SerializeValue, scylla::DeserializeValue)]",
    )
    .type_attribute(
      "service.v1.EmbedTwitch",
      "#[derive(scylla::SerializeValue, scylla::DeserializeValue)]",
    )
    .type_attribute(
      "service.v1.EmbedSpotify",
      "#[derive(scylla::SerializeValue, scylla::DeserializeValue)]",
    )
    .type_attribute(
      "service.v1.EmbedBandcamp",
      "#[derive(scylla::SerializeValue, scylla::DeserializeValue)]",
    )
    .type_attribute(
      "service.v1.EmbedAppleMusic",
      "#[derive(scylla::SerializeValue, scylla::DeserializeValue)]",
    )
    .type_attribute(
      "service.v1.EmbedStreamable",
      "#[derive(scylla::SerializeValue, scylla::DeserializeValue)]",
    )
    .type_attribute(
      "service.v1.EmbedText",
      "#[derive(scylla::SerializeValue, scylla::DeserializeValue)]",
    )
    .type_attribute(
      "shared.v1.StringArray",
      "#[derive(scylla::SerializeValue, scylla::DeserializeValue)]",
    )
    .type_attribute(
      "shared.v1.Timestamp",
      "#[derive(scylla::SerializeValue, scylla::DeserializeValue)]",
    )
    .type_attribute(
      "shared.v1.Empty",
      "#[derive(scylla::SerializeValue, scylla::DeserializeValue)]",
    )
    .type_attribute(
      "shared.v1.File",
      "#[derive(scylla::SerializeValue, scylla::DeserializeValue)]",
    )
    .type_attribute(
      "service.v1.Server",
      "#[derive(scylla::SerializeValue, scylla::DeserializeValue)]",
    )
    .type_attribute(
      "service.v1.Category",
      "#[derive(scylla::SerializeValue, scylla::DeserializeValue)]",
    )
    .type_attribute(
      "service.v1.ServerSystemMessagesChannels",
      "#[derive(scylla::SerializeValue, scylla::DeserializeValue)]",
    )
    .type_attribute(
      "service.v1.ServerStats",
      "#[derive(scylla::SerializeValue, scylla::DeserializeValue)]",
    )
    .file_descriptor_set_path(format!("{}/descriptor.bin", out_dir))
    .compile_protos(
      &[
        "shared/v1/error.proto",
        "shared/v1/files.proto",
        "shared/v1/pagination.proto",
        "shared/v1/struct.proto",
        "shared/v1/time.proto",
        "shared/v1/types.proto",
        "shared/v1/wrappers.proto",
        "service/v1/channels_db.proto",
        "service/v1/groups.proto",
        "service/v1/main.proto",
        "service/v1/messages.proto",
        "service/v1/messages_db.proto",
        "service/v1/roles_db.proto",
        "service/v1/search.proto",
        "service/v1/servers_db.proto",
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
