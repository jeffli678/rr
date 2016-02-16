from rrutil import *

send_gdb('handle SIGKILL stop')

send_gdb('c')
expect_gdb('SIGKILL')

send_gdb('watch -l x')
expect_gdb('Hardware[()/a-z ]+watchpoint 1')
send_gdb('break main')
expect_gdb('Breakpoint 2')

send_gdb('rc')
expect_gdb('Breakpoint 2')

ok()
