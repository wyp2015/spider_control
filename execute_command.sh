#!/usr/bin/expect

set ip [lindex $argv 0]
set user [lindex $argv 1]
set password [lindex $argv 2]
set exec_path [lindex $argv 3]

spawn ssh ${user}@${ip}
expect {
"*yes/no*" { send "yes\r"; exp_continue }
"*assword*" { send ${password}\r }
}
expect {
"*$*" {}
"*#*" {}
}

set command [lindex $argv 4]

send "cd ${exec_path}\r"
send "${command}\r"

send "exit\r"

interact
