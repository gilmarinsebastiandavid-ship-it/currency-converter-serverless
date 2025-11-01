import json
import urllib.request
import urllib.error

def lambda_handler(event, context):
    """
    Función Lambda que convierte entre dos monedas
    Recibe: from_currency, to_currency, amount
    Retorna: resultado de conversión y tasa usada
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
        # Obtener datos del body
        if event.get('body'):
            body = json.loads(event['body'])
        else:
            body = event.get('queryStringParameters', {})
        
        from_currency = body.get('from_currency', '').upper()
        to_currency = body.get('to_currency', '').upper()
        amount = float(body.get('amount', 0))
        
        # Validaciones
        if not from_currency or not to_currency:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({
                    'success': False,
                    'error': 'Debe especificar from_currency y to_currency'
                })
            }
        
        if amount <= 0:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({
                    'success': False,
                    'error': 'El monto debe ser mayor a 0'
                })
            }
        
        # Obtener tasas de cambio de la API
        api_url = f'https://api.exchangerate-api.com/v4/latest/{from_currency}'
        
        with urllib.request.urlopen(api_url, timeout=5) as response:
            data = json.loads(response.read().decode())
        
        # Verificar que la moneda destino existe
        if to_currency not in data['rates']:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({
                    'success': False,
                    'error': f'Moneda {to_currency} no soportada'
                })
            }
        
        # Realizar conversión
        rate = data['rates'][to_currency]
        converted_amount = amount * rate
        
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({
                'success': True,
                'from_currency': from_currency,
                'to_currency': to_currency,
                'amount': amount,
                'rate': round(rate, 4),
                'converted_amount': round(converted_amount, 2),
                'formatted': f"{amount:,.2f} {from_currency} = {converted_amount:,.2f} {to_currency}"
            })
        }
        
    except ValueError as e:
        return {
            'statusCode': 400,
            'headers': headers,
            'body': json.dumps({
                'success': False,
                'error': 'Formato de datos inválido',
                'details': str(e)
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