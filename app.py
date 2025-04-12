from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

def main():

    search_date = "1988-04-25"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(f"https://www.billboard.com/charts/hot-100/{search_date}")


    # lists to append the song titles and the artist names
    song_title_list = []
    artist_list = []

    # Get the parent container with xpath
    top_100_container = driver.find_element(By.XPATH, "//*[@id='post-1479786']/div[3]/div/div/div/div[2]")

    # Get all the list elements of the parent container that includes the song titles and artist names
    top_100_list = top_100_container.find_elements(By.XPATH, "./div/ul/li[4]/ul/li[1]")

    # itterate the list and get the song title by XPATH and the artist name by Class name
    # and append them to the lists
    for song in top_100_list:
        song_title = song.find_element(By.XPATH, ".//*[@id='title-of-a-story']")
        song_title_list.append(song_title.text)
        artist_name = song.find_element(By.CLASS_NAME, "c-label")
        artist_list.append(artist_name.text)

    driver.quit()

    # I will use Pandas just to create a df and export it easily to an excel file
    top_100_dict = {
        "artist": artist_list,
        "song": song_title_list
    }

    top_100_df = pd.DataFrame(top_100_dict)
    top_100_df.to_excel(f"top_100_{search_date.replace("-", "_")}.xlsx", sheet_name="top_100", index=None)

if __name__ == "__main__":
    main()