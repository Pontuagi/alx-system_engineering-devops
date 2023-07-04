#!/usr/bin/env ruby
# Regular expression must be only matching capital letters

regex = /[A-Z]/
input = ARGV[0]

match = input.scan(regex)
puts match.join("")
