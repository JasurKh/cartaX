Feature: Make API call to Open Weather based on the city name and validate it in the response.

  Scenario: Make API call to Open Weather by city name
    Given city names in the data folder
    When call API
    Then validate the response for city name

  Examples City names
    | names    |
    | New York |
    | London   |
    | Sydney   |

# bug with my PyCharm, behave is behaving, on the official website this issue still wasn't fixed since 2017
