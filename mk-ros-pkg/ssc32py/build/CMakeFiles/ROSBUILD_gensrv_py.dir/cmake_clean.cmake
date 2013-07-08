FILE(REMOVE_RECURSE
  "../srv_gen"
  "../src/ssc32py/srv"
  "CMakeFiles/ROSBUILD_gensrv_py"
  "../src/ssc32py/srv/__init__.py"
  "../src/ssc32py/srv/_None_Int32.py"
  "../src/ssc32py/srv/_MoveAng.py"
  "../src/ssc32py/srv/_None_Float.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
