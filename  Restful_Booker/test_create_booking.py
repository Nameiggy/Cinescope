import pytest
import requests

from constants import BASE_URL

class TestBookings:
    def test_create_booking(self, auth_session, booking_data):
        # Создаём бронирование
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, "Ошибка при создании брони"


        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "Идентификатор брони не найден в ответе"
        assert create_booking.json()["booking"]["firstname"] == booking_data["firstname"], "Заданное имя не совпадает"
        assert create_booking.json()["booking"]["totalprice"] == booking_data["totalprice"], "Заданная стоимость не совпадает"
        # Проверяем, что бронирование можно получить по ID
        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200, "Бронь не найдена"
        assert get_booking.json()["lastname"] == booking_data["lastname"], "Заданная фамилия не совпадает"

        # Удаляем бронирование
        deleted_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert deleted_booking.status_code == 201, "Бронь не удалилась"

        # Проверяем, что бронирование больше недоступно
        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 404, "Бронь не удалилась"

    def test_PUT_booking(self,auth_session,booking_data,new_booking):

        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200,"Ошибка при создании брони"

        booking_id = create_booking.json()["bookingid"]
        print(f"Создано бронирование #{booking_id}")

        print(f"2. Отправляю PUT запрос для бронирования #{booking_id}...")
        put_booking = auth_session.put(f"{BASE_URL}/booking/{booking_id}", json=new_booking)
        assert put_booking.status_code in [200, 201], \
            f"PUT запрос не удался: {put_booking.status_code} - {put_booking.text}"
        print(f"PUT запрос успешен (статус {put_booking.status_code})")

        get_resp = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        updated = get_resp.json()

        assert updated["firstname"] == new_booking["firstname"]
        print(f"Имя обновилось: '{updated['firstname']}'")
        assert updated["lastname"] == new_booking["lastname"]
        print(f"Фамилия обновилась:{updated["lastname"]}")
        assert updated["totalprice"] == new_booking["totalprice"]
        print(f"Стоимость обновилась: {updated['totalprice']}")
        assert updated["depositpaid"] == new_booking["depositpaid"]
        print(f"Депозит обновился: {updated["depositpaid"]}")
        assert updated["bookingdates"]["checkin"] == new_booking["bookingdates"]["checkin"]
        print(f"Дата брони обновилась : {updated["bookingdates"]}")
        assert updated["bookingdates"]["checkout"] == new_booking["bookingdates"]["checkout"]
        print(f"Дата брони обновилась: {updated["bookingdates"]}")
        assert updated["additionalneeds"] == new_booking["additionalneeds"]
        print(f"Новое: {updated["additionalneeds"]}")

        auth_session.delete(f"{BASE_URL}/booking/{booking_id}")


    def test_patch_response(self,auth_session,booking_data):

        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200,"Ошибка при создании брони"

        response = create_booking.json()
        booking_id = response.get("bookingid")
        print(f"Создано бронирование #{booking_id}")

        get_response = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        get_data = get_response.json()
        assert get_data["firstname"] == booking_data["firstname"]
        print(f"Имя :{get_data['firstname']}")
        assert get_data["lastname"] == booking_data["lastname"]
        print(f"Фамилия: {get_data['lastname']}")
        assert get_data["totalprice"] == booking_data["totalprice"]
        print(f"стоимость: {get_data['totalprice']}")
        assert get_data["depositpaid"] == booking_data["depositpaid"]
        print(f"Депозит: {get_data['depositpaid']}")
        assert get_data["bookingdates"] ["checkin"] == booking_data ["bookingdates"] ["checkin"]
        print(f'Бронь с: {get_data["bookingdates"]}')
        assert get_data["bookingdates"]["checkout"] == booking_data["bookingdates"]["checkout"]
        print(f'Бронь по: {get_data["bookingdates"]}')
        assert get_data["additionalneeds"] == booking_data["additionalneeds"]
        print(f"Дополнительно: {get_data["additionalneeds"]}")


        print(f"PATCH response")
        patch_response = auth_session.patch(f"{BASE_URL}/booking/{booking_id}",
                                              json ={"firstname": "Jon",
                                              "additionalneeds": "Apple" } )
        assert patch_response.status_code == 200



        get_patch_response = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        patch_data = get_patch_response.json()
        assert patch_data["firstname"] == "Jon"
        print(f"Имя изменено :{patch_data['firstname']}")
        assert patch_data["lastname"] == booking_data["lastname"]
        print(f"Фамилия: {patch_data['lastname']}")
        assert patch_data["totalprice"] == booking_data["totalprice"]
        print(f"стоимость: {patch_data['totalprice']}")
        assert patch_data["depositpaid"] == booking_data["depositpaid"]
        print(f"Депозит: {patch_data['depositpaid']}")
        assert patch_data["bookingdates"]["checkin"] == booking_data["bookingdates"]["checkin"]
        print(f'Бронь с: {patch_data["bookingdates"]}')
        assert patch_data["bookingdates"]["checkout"] == booking_data["bookingdates"]["checkout"]
        print(f'Бронь по: {patch_data["bookingdates"]}')
        assert patch_data["additionalneeds"] == "Apple"
        print(f"Дополнительно изменено : {patch_data["additionalneeds"]}")





