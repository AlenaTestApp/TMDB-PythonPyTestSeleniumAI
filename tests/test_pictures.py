
import pytest


@pytest.mark.parametrize(
    "artist, wiki_picture",
    [("Eric Bana", "wiki_pictures/Eric_Bana_at_the_2009_Tribeca_Film_Festival.jpg"),
     ("Liam Neeson", "wiki_pictures/Liam_Neeson_Deauville_2012_2.jpg"),
     ("Kelly Reilly", "wiki_pictures/Kelly_Reilly_2013.jpg"),
     ]
)
def test_picturs_comparison(artist_page, artist, wiki_picture):
    """Compare images from WiKipedia with images from Artist's Gallery collection"""
    threshold = 0.6
    failed = []
    artist_page.find_artist(artist)
    artist_page.open_artist_gallery(artist)
    image_urls = artist_page.collect_images()
    results = artist_page.compare_images(wiki_picture, image_urls)
    for url, simlrt in results:
        print(f"{url}: similarity = {simlrt:.4f}")
        if simlrt < threshold:
            failed.append((url, simlrt))
    assert not failed, f"This pictures didn't match the threshold {threshold}: {failed}"