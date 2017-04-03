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

#set lip [lindex $argv 3]
#set luser [lindex $argv 4]
#set lpassword [lindex $argv 5]

set upload_path [lindex $argv 3]
set download_path [lindex $argv 4]
set lpassword [lindex $argv 5]
set k [lindex $argv 6]

if { ${k} == "2" } {
	send "mkdir ${download_path}\r"
}
#send "mkdir ${server_path}\r"

send "scp -r ${upload_path} ${download_path}\r"
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
