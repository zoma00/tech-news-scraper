function main(splash, args)
  -- Wait for the page to load (adjust wait time as needed)
  splash.wait(5)
  splash.wait(wait_time)

  -- Access the passed selector argument
  local card_title_selector = args.card_title_selector

  -- Use the received selector to select archive items
  local archive_items = splash:select_all(card_title_selector)

  local data = {} -- Create an empty table to store extracted data

  for _, element in ipairs(archive_items) do
    -- Extract href
    local href = element.href
    if href then
      table.insert(data, { href = href }) -- Add href to data table
    end

    -- Extract title (using CSS selector)
    local title = element.css(".card-title::text").get()

    -- Extract description (using XPath)
    local description_xpath = ".//div[@class='card-result-card']//text()"
    local descriptions = splash:select_all(description_xpath)
    local description = table.concat(descriptions, " ") -- Join descriptions with a space

    -- Check if title and description are available (optional)
    if title and description then
      -- Update the data table entry with extracted title and description
      data[#data].title = title
      data[#data].description = description.strip() -- Strip leading/trailing whitespace
    end
  end

  return data -- Return the table containing extracted data
end
