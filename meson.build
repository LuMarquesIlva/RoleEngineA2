project('RoleEngineA2Tools', 'c', 'cpp', version: '0.0.1')

cmake = import('cmake')
appimagetool_opts = cmake.subproject_options()

appimagetool_opts.add_cmake_defines(
    {
        'ARCH': 'x84_64',
        }
    )

appimagetool_proj = cmake.subproject('AppImageTool', options: appimagetool_opts)

message('AppImagetool CMake targets:\n - ' + '\n - '.join(appimagetool_proj.target_list()))

appimagetool_dep = appimagetool_proj.target('appimagetool')
