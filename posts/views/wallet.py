import json
from django.http import JsonResponse
from django.db import transaction
from posts.models import Wallet



def post(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        sender_wallet_id = data.get('sender_wallet', '')
        recipient_wallet_id = data.get('recipient_wallet', '')
        amount = data.get('amount', '')

        if sender_wallet_id is None or recipient_wallet_id is None or amount is None:
            return JsonResponse({'message': 'Invalid data'}, status=400)
        
        try:
            sender_wallet = Wallet.objects.get(id=sender_wallet_id)
            recipient_wallet = Wallet.objects.get(id=recipient_wallet_id)

            with transaction.atomic():
                if sender_wallet.balance >= amount:
                    sender_wallet.balance -= amount
                    recipient_wallet.balance += amount
                    sender_wallet.save()
                    recipient_wallet.save()
                else:
                    raise Exception('Insufficient funds')
                return JsonResponse({'message': 'Funds transferred successfully'})
        except Wallet.DoesNotExist:
            return JsonResponse({'message': 'Wallet not found'}, status=404)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=400)
    return JsonResponse({'message': 'Invalid request method'}, status=400)













