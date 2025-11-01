import json
import urllib.request
import urllib.error

def lambda_handler(event, context):
    """
    Función Lambda que obtiene tasas de cambio actuales
    API: exchangerate-api.com (gratis, sin API key)
    """
    
    # Configurar CORS headers
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS'
    }
    
    # Manejar preflight request
    if event.get('httpMethod') == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({'message': 'CORS OK'})
        }
    
    try:
        # Obtener parámetro de moneda base (default: USD)
        query_params = event.get('queryStringParameters', {})
        base_currency = query_params.get('base', 'USD') if query_params else 'USD'
        
        # Llamar a API externa
        api_url = f'https://api.exchangerate-api.com/v4/latest/{base_currency}'
        
        with urllib.request.urlopen(api_url, timeout=5) as response:
            data = json.loads(response.read().decode())
        
        # Extraer tasas relevantes
        rates = {
            'USD': data['rates'].get('USD', 1.0),
            'EUR': data['rates'].get('EUR', 0.85),
            'COP': data['rates'].get('COP', 4000.0),
            'GBP': data['rates'].get('GBP', 0.73),
            'JPY': data['rates'].get('JPY', 110.0)
        }
        
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({
                'success': True,
                'base': base_currency,
                'rates': rates,
                'timestamp': data.get('time_last_updated', '')
            })
        }
        
    except urllib.error.URLError as e:
        return {
            'statusCode': 503,
            'headers': headers,
            'body': json.dumps({
                'success': False,
                'error': 'No se pudo conectar con el servicio de tasas de cambio',
                'details': str(e)
            })
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({
                'success': False,
                'error': 'Error interno del servidor',
                'details': str(e)
            })
        }