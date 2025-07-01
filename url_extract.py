from urllib.parse import urlparse
import re
def extract_website_name(url):
    url="https://amazon.in/Minimalist-Sunscreen-Multi-Vitamins-Cream/dp/B09FPS9D5T?pd_rd_w=dZrdy&content-id=amzn1.sym.4c241eba-0ce0-4f45-a17d-f017b3203e3d&pf_rd_p=4c241eba-0ce0-4f45-a17d-f017b3203e3d&pf_rd_r=TMJBK8MS6XEEWBXYWACA&pd_rd_wg=pqsaf&pd_rd_r=548a6094-8538-44c6-96d5-7cd4449d5433&pd_rd_i=B09FPS9D5T&ref_=pd_bap_d_grid_rp_0_1_ec_nped_pr_pd_hp_d_atf_rp_2_t&th="
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    match = re.search(r"(?:www\.)?([a-zA-Z0-9-]+)", domain)
    website_name = match.group(1) if match else "unknown"
    return website_name