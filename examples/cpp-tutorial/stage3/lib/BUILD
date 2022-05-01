load("@rules_cc//cc:defs.bzl", "cc_library")

# cc_library(
#     name = "hello-time",
#     srcs = ["hello-time.cc"],
#     hdrs = ["hello-time.h"],
#     visibility = ["//main:__pkg__"],
# )

cc_library(
    name = "hello-time",
    srcs = glob(["*-time.cc"]),
    hdrs = glob(["*-time.h"]),
    visibility = ["//main:__pkg__"],
)