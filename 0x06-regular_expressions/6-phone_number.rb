#!/usr/bin/env ruby
#regular expression must match a 10 digit phone number

regex = /\b\d{10}\b(?!.*\d)/
input = ARGV[0]

matches = input.scan(regex)
puts matches.join("\n")
