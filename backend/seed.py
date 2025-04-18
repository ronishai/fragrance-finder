from app import app, db
from models import Fragrance, Note, FragranceType

def seed_database():
    with app.app_context():
        # Clear existing data
        db.session.query(Fragrance).delete()
        db.session.query(Note).delete()
        db.session.query(FragranceType).delete()
        db.session.commit()
        
        print("Creating fragrance types... ")
        # Create fragrance types
        types = {
            "Woody": FragranceType(name="Woody"),
            "Oriental": FragranceType(name="Oriental"),
            "Floral": FragranceType(name="Floral"),
            "Fresh": FragranceType(name="Fresh"),
            "Aromatic": FragranceType(name="Aromatic"),
            "Citrus": FragranceType(name="Citrus"),
            "Fougere": FragranceType(name="Fougere"),
            "Chypre": FragranceType(name="Chypre"),
            "Gourmand": FragranceType(name="Gourmand"),
            "Aquatic": FragranceType(name="Aquatic"),
            "Green": FragranceType(name="Green"),
            "Leather": FragranceType(name="Leather"),
            "Spicy": FragranceType(name="Spicy"),
            "Fruity": FragranceType(name="Fruity"),
        }
        
        for type_obj in types.values():
            db.session.add(type_obj)
        db.session.commit()
        
        print("Creating notes...")
        # Create notes
        notes = {
            "Top": Note(name="Top"),
            "Heart": Note(name="Heart"),
            "Base": Note(name="Base"),
        }
        
        for note_obj in notes.values():
            db.session.add(type_obj)
        
        print("Creating fragrances...")
        # Create common notes
        notes = {}
        common_notes = [
            # Citruses
            ("Bergamot", "Citrus"), ("Lemon", "Citrus"), ("Orange", "Citrus"), ("Lime", "Citrus"), 
            ("Mandarin", "Citrus"), ("Grapefruit", "Citrus"),
            
            # Florals
            ("Rose", "Floral"), ("Lavender", "Floral"), ("Jasmine", "Floral"), 
            ("Lily-of-the-Valley", "Floral"), ("Violet", "Floral"), ("Ylang-Ylang", "Floral"),
            ("Tuberose", "Floral"), ("Geranium", "Floral"),
            
            # Woods
            ("Cedar", "Woody"), ("Sandalwood", "Woody"), ("Vetiver", "Woody"),
            ("Oud", "Woody"), ("Patchouli", "Woody"), ("Birch", "Woody"),
            
            # Spices
            ("Cinnamon", "Spicy"), ("Clove", "Spicy"), ("Pink Pepper", "Spicy"), ("Nutmeg", "Spicy"),
            ("Cardamom", "Spicy"), ("Black Pepper", "Spicy"),
            
            # Fruits
            ("Apple", "Fruity"), ("Pear", "Fruity"), ("Peach", "Fruity"), ("Plum", "Fruity"),
            ("Pineapple", "Fruity"), ("Strawberry", "Fruity"), ("Raspberry", "Fruity"),
            ("Coconut", "Fruity"),
            
            # Gourmand
            ("Vanilla", "Gourmand"), ("Caramel", "Gourmand"), ("Cocoa", "Gourmand"),
            ("Coffee", "Gourmand"), ("Mint", "Gourmand"), ("Peppermint", "Gourmand"),
            ("Almond", "Gourmand"), ("Praline", "Gourmand"), ("Tonka Bean", "Gourmand"),
            
            # Others
            ("Musk", "Animalic"), ("Amber", "Resin"), ("Incense", "Resin"),
            ("Marine Notes", "Aquatic"), ("Leather", "Animalic")
        ]
        
        for name, category in common_notes:
            note = Note(name=name, category=category)
            notes[name] = note
            db.session.add(note)
            
        print("Creating fragrances...")
        # Create sample fragrances
        fragrances = [
            {
                "name": "Bleu de Chanel",
                "brand": "Chanel",
                "release_year": 2010,
                "gender": "Men",
                "concentration": "Eau de Parfum",
                "description": "A woody aromatic fragrance for the man who defies convention.",
                "image_url": "https://www.chanel.com/images//t_one//w_0.51,h_0.51,c_crop/q_auto:good,f_autoplus,fl_lossy,dpr_1.1/w_1240/bleu-de-chanel-eau-de-parfum-spray-3-4fl-oz--packshot-default-107360-9564894232606.jpg",
                "notes": ["Bergamot", "Lemon", "Pink Pepper", "Grapefruit", "Jasmine", 
                          "Nutmeg", "Cedar", "Incense", "Vetiver"],
                "types": ["Aromatic", "Woody"]
            },
            {
                "name": "Sauvage",
                "brand": "Dior",
                "gender": "Men",
                "concentration": "Eau de Toilette",
                "release_year": 2015,
                "description": "A radically fresh composition, dictated by a name that has the ring of a manifesto.",
                "image_url": "https://www.dior.com/dw/image/v2/BGXS_PRD/on/demandware.static/-/Sites-master_dior/default/dw8b0b4965/Y0685240/Y0685240_F068524009_E01_ZHC.jpg?sw=1920",
                "notes": ["Bergamot", "Black Pepper", "Geranium", "Lavender", 
                         "Pink Pepper", "Vetiver", "Patchouli"],
                "types": ["Aromatic", "Fougere"]
            },
            {
                "name": "Acqua di Giò",
                "brand": "Giorgio Armani",
                "gender": "Men",
                "concentration": "Eau de Toilette",
                "release_year": 1996,
                "description": "Inspired by the beauty of the Mediterranean Sea.",
                "image_url": "https://www.giorgioarmanibeauty-usa.com/dw/image/v2/AANG_PRD/on/demandware.static/-/Sites-gab-master-catalog/default/dw04d58b00/products/2025/A005%20RESTAGE/3614273955546_01.jpg?sw=1442&sh=1442&sm=cut&sfrm=jpg&q=85",
                "notes": ["Marine Notes", "Bergamot", "Lemon", "Jasmine", "Cedar", "Musk"],
                "types": ["Aquatic", "Fresh"]
            },
            {
                "name": "Black Opium",
                "brand": "Yves Saint Laurent",
                "gender": "Women",
                "concentration": "Eau de Parfum",
                "release_year": 2014,
                "description": "The highly addictive feminine fragrance from Yves Saint Laurent.",
                "image_url": "https://www.yslbeautyus.com/dw/image/v2/AANG_PRD/on/demandware.static/-/Sites-ysl-master-catalog/default/dwf7216072/Black%20Opium%20Packshots/BO%20EDP/3365440787971.jpg?sw=1440&sh=1440&sm=cut&sfrm=jpg&q=85", 
                "notes": ["Coffee", "Vanilla", "Orange Blossom", "Jasmine", "Cedar", "Patchouli"],
                "types": ["Oriental", "Gourmand"]
            },
            {
                "name": "Light Blue",
                "brand": "Dolce & Gabbana",
                "gender": "Women",
                "concentration": "Eau de Toilette",
                "release_year": 2001,
                "description": "The joy of living the Light Blue Mediterranean life.",
                "image_url": "https://www.dolcegabbana.com/dw/image/v2/BKDB_PRD/on/demandware.static/-/Sites-15/default/dw1fac626f/images/zoom/VT01CPVT000_9V000_0.jpg",
                "notes": ["Apple", "Cedar", "Lemon", "Jasmine", "Rose", "Amber"],
                "types": ["Citrus", "Floral"]
            },
            {
                "name": "Aventus",
                "brand": "Creed",
                "gender": "Men",
                "concentration": "Eau de Parfum",
                "release_year": 2010,
                "description": "Celebrates strength, vision and success.",
                "image_url": "https://creedboutique.com/cdn/shop/files/aventus-100ml-bottle_3413e5f4-3eee-40b3-8451-2546a370ec5b.jpg?v=1734710265&width=1500",
                "notes": ["Pineapple", "Bergamot", "Blackcurrant", "Apple", "Rose", "Birch", "Musk", "Oakmoss"],
                "types": ["Fruity", "Woody"]
            },
            {
                "name": "J'adore",
                "brand": "Dior",
                "gender": "Women",
                "concentration": "Eau de Parfum",
                "release_year": 1999,
                "description": "The absolute femininity in a sumptuous floral bouquet.",
                "image_url": "https://www.dior.com/dw/image/v2/BGXS_PRD/on/demandware.static/-/Sites-master_dior/default/dwfd90a551/Y0998031/Y0998031_C099800246_E01_ZHC.jpg?sw=1920",
                "notes": ["Ylang-Ylang", "Rose", "Jasmine", "Tuberose", "Lily-of-the-Valley"],
                "types": ["Floral"]
            }
        ]
        
        for fragrance_data in fragrances:
            fragrance = Fragrance(
                name=fragrance_data["name"],
                brand=fragrance_data["brand"],
                gender=fragrance_data["gender"],
                concentration=fragrance_data["concentration"],
                release_year=fragrance_data["release_year"],
                description=fragrance_data["description"],
                image_url=fragrance_data["image_url"]
            )
            
            for note_name in fragrance_data["notes"]:
                if note_name in notes:
                    fragrance.notes.append(notes[note_name])
                else:
                    new_note = Note(name=note_name, category="Other")
                    db.session.add(new_note)
                    fragrance.notes.append(new_note)
                    
            # Add types to fragrance
            for type_name in fragrance_data["types"]:
                if type_name in types:
                    fragrance.types.append(types[type_name])
                
            
            db.session.add(fragrance)
            
        db.session.commit()
        print("Databases seeded successfully!")
        
if __name__ == '__main__':
    seed_database()
        
        