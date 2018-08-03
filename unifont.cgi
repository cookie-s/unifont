#!/usr/bin/env ruby

#vim: ft=ruby

puts 'Content-Type: text/plain'
puts ''

dict = {}
File.open("unifont-10.0.06.hex.gz") do |f|
  f.each_line do |l|
    cp, bmp = l.chomp.split(":")
    dict[cp.hex] = [bmp.hex, bmp.size * 4]
  end
end

qs = ENV['QUERY_STRING'][1,100]
puts qs.codepoints.map{ |cp|
  bmp, sz = dict[cp]
  bmp.to_s(2).rjust(sz,?0).gsub(/[01]/, {'0' => '_', '1' => '#'}).scan(%r(.{#{sz/16}}))
}.transpose.map(&:join).join("\n")
