source "https://rubygems.org"

# Use GitHub Pages gem instead of Jekyll gem
gem "github-pages", group: :jekyll_plugins

# This is the default theme for new Jekyll sites. You may change this to anything you like.
gem "minima", "~> 2.5"

# If you have any plugins, put them here!
group :jekyll_plugins do
  gem "jekyll-admin", "~> 0.11"
  gem "jekyll-feed", "~> 0.12"
  gem "csv", "~> 3.1"
  gem "webrick", "~> 1.7"
  gem "rack", "~> 2.2"
end

# Windows and JRuby does not include zoneinfo files, so bundle the tzinfo-data gem
# and associated library.
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Lock `http_parser.rb` gem to `v0.6.x` on JRuby builds since newer versions of the gem
# do not have a Java counterpart.
gem "http_parser.rb", "~> 0.6.0", :platforms => [:jruby]

# Performance-booster for watching directories on Windows (optional, may cause issues)
# gem "wdm", ">= 0.1.0", :platforms => [:mingw, :x64_mingw, :mswin]
