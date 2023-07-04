#!/usr/bin/env ruby
# Output sender, receiver, flags

regex_from = /from:([^\[\]]+)/
regex_to = /to:([^\[\]]+)/
regex_flag = /flags:(-?\d+:-?\d+:-?\d+:-?\d+:-?\d+)/

input = ARGV[0]

sender = input.match(regex_from)&.captures&.first
receiver = input.match(regex_to)&.captures&.first
flags = input.match(regex_flag)&.captures&.first
puts "#{sender},#{receiver},#{flags}"
