#!/usr/bin/env ruby

require 'uri'

puts 'Content-Type: text/html'
puts ''


dict = {}
File.open("unifont.hex") do |f|
  f.each_line do |l|
    cp, bmp = l.chomp.split(":")
    dict[cp.hex] = [bmp.hex, bmp.size * 4]
  end
end

qs = ENV['QUERY_STRING']
qs = 'イワシ' unless qs && !qs.empty?
qs = URI.decode(qs).force_encoding("UTF-8")
qs = qs[0,100]


puts '<html><body>'
puts '<p><a href="https://github.com/cookie-s/unifont">source</a></p>'
puts %q(<form onsubmit="location.href = '?' + encodeURIComponent(document.getElementById('text').value); return false;"> <input id="text" type="text" /> <input type="submit" /> </form>)

puts '<pre>'

puts qs.codepoints.map{ |cp|
  bmp, sz = dict[cp] || [0, 256]
  bmp.to_s(2).rjust(sz,?0).scan(%r(.{#{sz/16}}))
}.transpose.map(&:join).join("\n")

puts ''
puts ''
puts ''

puts qs.codepoints.map{ |cp|
  bmp, sz = dict[cp] || [0, 256]
  bmp.to_s(2).rjust(sz,?0).scan(%r(.{#{sz/16}}))
}.transpose.map(&:join).join("\n").gsub(/[01]/, {'0' => '_', '1' => '#'})

puts ''
puts ''
puts ''

puts qs.codepoints.map{ |cp|
  bmp, sz = dict[cp] || [0, 256]
  bmp.to_s(2).rjust(sz,?0).scan(%r(.{#{sz/16}}))
}.transpose.map(&:join).join("\n").gsub(/[01]/, {'0' => '__', '1' => '##'})


puts ''
puts ''
puts ''

puts '</pre>'

puts '</body></html>'
