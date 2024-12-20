### plot all datafiles in a directory
# https://stackoverflow.com/questions/60963846/script-to-launch-gnuplot-and-plot-graph
# gnuplot -p test.gp

reset session
set term pngcairo

DIR   = ''     # 'Test/' directory; use '' for current directory
EXT   = '.arc_data'      # file extension
FILES = GPVAL_SYSNAME[1:7] eq 'Windows' ? system(sprintf('dir /B %s*%s',DIR,EXT)) : \
                                          system(sprintf('ls     %s*%s',DIR,EXT))     # Linux/MacOS

myInput(s)  = sprintf('%s%s',DIR,s)
myOutput(s) = sprintf('%s%s.png',DIR,s[1:strlen(s)-strlen(EXT)])    # replace file extension with .png

do for [FILE in FILES] {
    set output myOutput(FILE)
    plot myInput(FILE) u 1:2 w lines lc "red" title FILE
}
set output
### end of script