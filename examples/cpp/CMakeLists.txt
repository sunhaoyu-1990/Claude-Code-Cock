cmake_minimum_required(VERSION 3.14)
project(cpp_example VERSION 1.0.0 LANGUAGES CXX)

# C++17 标准
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# 编译选项
if(MSVC)
    add_compile_options(/W4)
else()
    add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# 源文件
set(SOURCES
    src/calculator.cpp
)

# 头文件
set(HEADERS
    include/cpp_example/calculator.h
)

# 创建库
add_library(cpp_example ${SOURCES})
target_include_directories(cpp_example PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
)

# 启用测试
enable_testing()
find_package(GTest REQUIRED)

# 测试源文件
set(TEST_SOURCES
    tests/calculator_test.cpp
)

# 创建测试可执行文件
add_executable(cpp_example_tests ${TEST_SOURCES})
target_link_libraries(cpp_example_tests
    cpp_example
    GTest::GTest
    GTest::Main
)

include(GoogleTest)
gtest_discover_tests(cpp_example_tests)
