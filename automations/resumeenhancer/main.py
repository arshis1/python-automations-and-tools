import logging
import keyword_extractor as ke
import url_to_text_extractor as ute

if __name__ == "__main__":
    url = input("Enter the URL: ")
    #url = "https://alteryx.wd5.myworkdayjobs.com/en-US/AlteryxCareers/job/Technical-Account-Manager_R10884?locationCountry=bc33aa3152ec42d4995f4791a106ed09"
    extracted_metadata = ute.extract_all_meta_from_url(url)
    if extracted_metadata:
        print("\nExtracted Metadata:\n")
        for key, value in extracted_metadata.items():
            print(f"{key}: {value}")
    
    print(ke.extract_keywords(extracted_metadata['description'], top_n=20))

    
