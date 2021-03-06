cmake_minimum_required(VERSION 3.8 FATAL_ERROR)
project(spine C)

include(${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_library(spine-c STATIC
  Animation.c
  AnimationState.c
  AnimationStateData.c
  Array.c
  Atlas.c
  AtlasAttachmentLoader.c
  Attachment.c
  AttachmentLoader.c
  Bone.c
  BoneData.c
  BoundingBoxAttachment.c
  ClippingAttachment.c
  Color.c
  Event.c
  EventData.c
  IkConstraint.c
  IkConstraintData.c
  Json.c
  MeshAttachment.c
  PathAttachment.c
  PathConstraint.c
  PathConstraintData.c
  PointAttachment.c
  RegionAttachment.c
  Skeleton.c
  SkeletonBinary.c
  SkeletonBounds.c
  SkeletonClipping.c
  SkeletonData.c
  SkeletonJson.c
  Skin.c
  Slot.c
  SlotData.c
  TransformConstraint.c
  TransformConstraintData.c
  Triangulator.c
  VertexAttachment.c
  VertexEffect.c
  extension.c
)



target_include_directories(spine-c PRIVATE ${CMAKE_CURRENT_SOURCE_DIR} spine)
target_compile_definitions(spine-c PRIVATE -D_CRT_SECURE_NO_WARNINGS)
