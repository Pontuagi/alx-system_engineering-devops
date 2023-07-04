#!/usr/bin/env ruby
# Ruby script that accepts one argument and pass it to a regular expression matching method

token = /hbt+n/
input = ARGV[0]

match = input.scan(token)
puts match.join("\n")
