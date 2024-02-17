require 'yaml'
require 'fileutils'

module Jekyll
  class YamlPage < Page
    def initialize(site, base, dir, name, yaml_content)
      @site = site
      @base = base
      @dir = dir
      @name = name

      self.process(@name)
      self.read_yaml(File.join(base, '_layouts'), 'person.liquid') # Ensure this matches your layout file's name
      self.data['page_data'] = yaml_content # Pass the whole YAML content
    end
  end

  class YamlPageGenerator < Generator
    safe true
    priority :low

    def generate(site)
        puts "\nStarting YAML page generation...\n"
        
        dir = 'people'
        path = '_data/people' # Adjust this path if your YAML files are located elsewhere
        FileUtils.mkdir_p(File.join(site.source, dir)) unless File.exist?(File.join(site.source, dir))
        yaml_files = Dir.glob(File.join(site.source, path, '*.{yml,yaml}')) # Retrieve all .yaml files
        
        # Print out each file path
        puts "Found YAML files:"
        yaml_files.each { |file| puts file }

        yaml_files.each do |file| # Iterate over each .yaml file
            yaml_content = YAML.load_file(file)
            file_extension = File.extname(file)
            name = File.basename(file, file_extension)
            puts "Generating page for: #{name}"
            site.pages << YamlPage.new(site, site.source, dir, "#{name}.html", yaml_content)
        end
    end
  end
end
