from flask import request, jsonify
from app import app, db
from models import Fragrance, Note, FragranceType  
from sqlalchemy import or_

def calculate_similarity(fragrance1, fragrance2):
    notes1 = set(note.id for note in fragrance1.notes)
    notes2 = set(note.id for note in fragrance2.notes)
    
    intersection = len(notes1.intersection(notes2))
    union = len(notes1.union(notes2))
    note_similarity = intersection / union if union > 0 else 0
    
    types1 = set(type.id for type in fragrance1.types)
    types2 = set(type.id for type in fragrance2.types)
    tyoe_intersection = len(types1.intersection(types2))
    type_similarity = type_intersection / max(len(types_a), len(types_b)) if max(len(types_a), len(types_b)) > 0 else 0
    
    total_similarity = (note_similarity + type_similarity) / 2
    return total_similarity * 100

@app.route('/')
def index():
    return jsonify({'message': Welcome to Fragrance Finder!})'})

@app.route('/api/search', methods=['GET'])
def search_fragrances():
    query = request.args.get('q', '')
    if len(query) < 3:
        return jsonify({'error': 'Query must be at least 3 characters long.'}), 400
        
    fragrances = Fragrance.query.filter(
        or_(
            Fragrance.name.ilike(f'%{query}%'), 
            Fragrance.brand.ilike(f'%{query}%'))
        ).limit(10).all()
        
        return jsonify({
            "results": [
                {
                    "id": fragrance.id,
                    "name": fragrance.name,
                    "brand": fragrance.brand
                    "image_url": fragrance.image_url
                } for fragrance in fragrances
            ]
        })
        
@app.route('/api/fragrance/<int:id>', methods=['GET'])
def get_fragrance(id):
    fragrance = Fragrance.query.get_or_404(id)
    return jsonify(fragrance.to_dict())
    
@app.route('/api/fragrance/<int:id>/similar', methods=['GET'])
def similar_fragrances(id):
    fragrance = Fragrance.query.get_or_404(id)
    all_fragrances = Fragrance.query.filter(Fragrance.id != id).all()
    similar_fragrances = []
    for f in all_fragrances:
        similarity = calculate_similarity(fragrance, f)
        if similarity > 20: # Only include fragrances with similarity score > 20
            similar_fragrances.append({
                "id": f.id,
                "name": f.name,
                "brand": f.brand,
                "image_url": f.image_url,
                "similarity": round(similarity, 1)
                "notes": [n.name for n in f.notes][:5], # Get the first 5 notes
                "types": [t.name for t in f.types]
            })
    similar_fragrances.sort(key=lambda x: x['similarity'], reverse=True) # Sort by similarity in descending order
    return jsonify({
        "fragrances": {
            "id": fragrance.id,
            "name": fragrance.name,
            "brand": fragrance.brand,
            "image_url": fragrance.image_url,
            "notes": [n.name for n in fragrance.notes]
            "types": [t.name for t in fragrance.types]
        },
        "similar_fragrances": similar_fragrances [:6] # Get the first 6 similar fragrances
    })


