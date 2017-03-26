#!/usr/bin/expect

set user [lindex $argv 0]
set password [lindex $argv 1]
set ip [lindex $argv 2]

spawn ssh ${user}@${ip}
expect {
"*yes/no*" { send "yes\r"; exp_continue }
"*assword*" { send ${password}\r }
}
expect {
"*$*" {}
"*#*" {}
}


send "nohup ./test.sh &\n"

send "exit\r"

interact
