#!/usr/bin/expect

set ip [lindex $argv 0]
set user [lindex $argv 1]
set password [lindex $argv 2]

spawn ssh ${user}@${ip}
expect {
"*yes/no*" { send "yes\r"; exp_continue }
"*assword*" { send ${password}\r }
}
expect {
"*$*" {}
"*#*" {}
}

set lip [lindex $argv 3]
set luser [lindex $argv 4]
set lpassword [lindex $argv 5]

set client_path [lindex $argv 6]
set server_path [lindex $argv 7]

send "mkdir ${server_path}\r"

send "scp -r ${luser}@${lip}:${client_path} ${server_path}\r"
expect {
	"*yes/no*" {send "yes\r"; exp_continue}
	"*assword*" { send ${lpassword}\r }
}
expect {
	"*$*" {send "exit\r"}
	"*#*" {send "exit\r"}
}

#send "exit\r"

interact
