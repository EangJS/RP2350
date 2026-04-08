cmake_minimum_required(VERSION 3.13...3.27)

if(NOT DEFINED PICO_BOARD)
    set(PICO_BOARD pico2 CACHE STRING "Pico board type")
endif()

# initialize pico-sdk from submodule
# note: this must happen before project()
include(vendor/pico-sdk/pico_sdk_init.cmake)

project(my_project)

# initialize the Raspberry Pi Pico SDK
pico_sdk_init()

add_executable(pico_project
    src/entrypoint.c
)

# Add SEGGER RTT library
add_library(segger_rtt
    vendor/SEGGER_RTT/RTT/SEGGER_RTT.c
    vendor/SEGGER_RTT/RTT/SEGGER_RTT_printf.c
)

target_include_directories(segger_rtt PUBLIC
    ${CMAKE_CURRENT_LIST_DIR}/vendor/SEGGER_RTT/RTT
    ${CMAKE_CURRENT_LIST_DIR}/vendor/SEGGER_RTT/Config
)

target_include_directories(pico_project PUBLIC
    ${CMAKE_CURRENT_LIST_DIR}/vendor/pico-sdk/src/rp2_common/cmsis/stub/CMSIS/Core/Include
    ${CMAKE_CURRENT_LIST_DIR}/vendor/pico-sdk/src/rp2_common/cmsis/stub/CMSIS/Device/RP2350/Include
)

target_link_libraries(pico_project pico_stdlib segger_rtt)

pico_add_extra_outputs(pico_project)
