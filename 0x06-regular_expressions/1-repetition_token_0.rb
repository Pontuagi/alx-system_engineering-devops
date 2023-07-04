#!/usr/bin/env ruby
# Ruby script that accepts one argument and pass it to a regular expression matching method

regex = /(hb(t{2,5})n)/
input = ARGV[0]

matches = input.scan(regex)
puts matches.join("\n")
