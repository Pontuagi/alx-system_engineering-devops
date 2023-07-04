#!/usr/bin/env ruby
# Ruby script that accepts one argument and pass it to a regular expression matching method
# The regular expression should be a string starting with h and ends with n

regex = /^h.n$/
input = ARGV[0]

matches = input.scan(regex)
puts matches.join("\n")
