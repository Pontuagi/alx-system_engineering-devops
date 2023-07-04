#!/usr/bin/env ruby
#regular expression must match a 10 digit phone number

regex = /\d{10}/
input = ARGV[0]

matches = input.scan(regex)
puts matches.join("\n")
