# coding: utf-8

from __future__ import absolute_import

# import OcrClient
from huaweicloudsdkocr.v1.ocr_client import OcrClient
from huaweicloudsdkocr.v1.ocr_async_client import OcrAsyncClient
# import models into sdk package
from huaweicloudsdkocr.v1.model.auto_classification_req import AutoClassificationReq
from huaweicloudsdkocr.v1.model.auto_classification_response_body_item import AutoClassificationResponseBodyItem
from huaweicloudsdkocr.v1.model.bankcard_req import BankcardReq
from huaweicloudsdkocr.v1.model.bankcard_result_body import BankcardResultBody
from huaweicloudsdkocr.v1.model.business_card_items_response import BusinessCardItemsResponse
from huaweicloudsdkocr.v1.model.business_card_req import BusinessCardReq
from huaweicloudsdkocr.v1.model.business_card_response_body_item import BusinessCardResponseBodyItem
from huaweicloudsdkocr.v1.model.business_license_req import BusinessLicenseReq
from huaweicloudsdkocr.v1.model.business_license_result_body import BusinessLicenseResultBody
from huaweicloudsdkocr.v1.model.flight_itinerary_items_response import FlightItineraryItemsResponse
from huaweicloudsdkocr.v1.model.flight_itinerary_req import FlightItineraryReq
from huaweicloudsdkocr.v1.model.flight_itinerary_response_body_item import FlightItineraryResponseBodyItem
from huaweicloudsdkocr.v1.model.general_text_items_response import GeneralTextItemsResponse
from huaweicloudsdkocr.v1.model.general_text_req import GeneralTextReq
from huaweicloudsdkocr.v1.model.general_text_response_body_items import GeneralTextResponseBodyItems
from huaweicloudsdkocr.v1.model.handwriting_items2_response import HandwritingItems2Response
from huaweicloudsdkocr.v1.model.handwriting_items3_response import HandwritingItems3Response
from huaweicloudsdkocr.v1.model.handwriting_items4_response import HandwritingItems4Response
from huaweicloudsdkocr.v1.model.handwriting_items_response import HandwritingItemsResponse
from huaweicloudsdkocr.v1.model.handwriting_req import HandwritingReq
from huaweicloudsdkocr.v1.model.handwriting_response_body_item import HandwritingResponseBodyItem
from huaweicloudsdkocr.v1.model.id_card_req import IDCardReq
from huaweicloudsdkocr.v1.model.id_card_result_body import IDCardResultBody
from huaweicloudsdkocr.v1.model.license_plate_req import LicensePlateReq
from huaweicloudsdkocr.v1.model.license_plate_response_body_item import LicensePlateResponseBodyItem
from huaweicloudsdkocr.v1.model.mvs_invoice_req import MvsInvoiceReq
from huaweicloudsdkocr.v1.model.mvs_invoice_result_body import MvsInvoiceResultBody
from huaweicloudsdkocr.v1.model.passport_req import PassportReq
from huaweicloudsdkocr.v1.model.passport_result_body import PassportResultBody
from huaweicloudsdkocr.v1.model.quota_invoice_req import QuotaInvoiceReq
from huaweicloudsdkocr.v1.model.quota_invoice_result_body import QuotaInvoiceResultBody
from huaweicloudsdkocr.v1.model.recognize_auto_classification_request import RecognizeAutoClassificationRequest
from huaweicloudsdkocr.v1.model.recognize_auto_classification_response import RecognizeAutoClassificationResponse
from huaweicloudsdkocr.v1.model.recognize_bankcard_request import RecognizeBankcardRequest
from huaweicloudsdkocr.v1.model.recognize_bankcard_response import RecognizeBankcardResponse
from huaweicloudsdkocr.v1.model.recognize_business_card_request import RecognizeBusinessCardRequest
from huaweicloudsdkocr.v1.model.recognize_business_card_response import RecognizeBusinessCardResponse
from huaweicloudsdkocr.v1.model.recognize_business_license_request import RecognizeBusinessLicenseRequest
from huaweicloudsdkocr.v1.model.recognize_business_license_response import RecognizeBusinessLicenseResponse
from huaweicloudsdkocr.v1.model.recognize_driver_license_request import RecognizeDriverLicenseRequest
from huaweicloudsdkocr.v1.model.recognize_driver_license_request_body import RecognizeDriverLicenseRequestBody
from huaweicloudsdkocr.v1.model.recognize_driver_license_response import RecognizeDriverLicenseResponse
from huaweicloudsdkocr.v1.model.recognize_driver_license_result_response import RecognizeDriverLicenseResultResponse
from huaweicloudsdkocr.v1.model.recognize_flight_itinerary_request import RecognizeFlightItineraryRequest
from huaweicloudsdkocr.v1.model.recognize_flight_itinerary_response import RecognizeFlightItineraryResponse
from huaweicloudsdkocr.v1.model.recognize_general_table_items2_response import RecognizeGeneralTableItems2Response
from huaweicloudsdkocr.v1.model.recognize_general_table_items_response import RecognizeGeneralTableItemsResponse
from huaweicloudsdkocr.v1.model.recognize_general_table_request import RecognizeGeneralTableRequest
from huaweicloudsdkocr.v1.model.recognize_general_table_request_body import RecognizeGeneralTableRequestBody
from huaweicloudsdkocr.v1.model.recognize_general_table_response import RecognizeGeneralTableResponse
from huaweicloudsdkocr.v1.model.recognize_general_table_result_response import RecognizeGeneralTableResultResponse
from huaweicloudsdkocr.v1.model.recognize_general_text_request import RecognizeGeneralTextRequest
from huaweicloudsdkocr.v1.model.recognize_general_text_response import RecognizeGeneralTextResponse
from huaweicloudsdkocr.v1.model.recognize_handwriting_request import RecognizeHandwritingRequest
from huaweicloudsdkocr.v1.model.recognize_handwriting_response import RecognizeHandwritingResponse
from huaweicloudsdkocr.v1.model.recognize_id_card_request import RecognizeIDCardRequest
from huaweicloudsdkocr.v1.model.recognize_id_card_response import RecognizeIDCardResponse
from huaweicloudsdkocr.v1.model.recognize_license_plate_request import RecognizeLicensePlateRequest
from huaweicloudsdkocr.v1.model.recognize_license_plate_response import RecognizeLicensePlateResponse
from huaweicloudsdkocr.v1.model.recognize_mvs_invoice_request import RecognizeMvsInvoiceRequest
from huaweicloudsdkocr.v1.model.recognize_mvs_invoice_response import RecognizeMvsInvoiceResponse
from huaweicloudsdkocr.v1.model.recognize_passport_request import RecognizePassportRequest
from huaweicloudsdkocr.v1.model.recognize_passport_response import RecognizePassportResponse
from huaweicloudsdkocr.v1.model.recognize_quota_invoice_request import RecognizeQuotaInvoiceRequest
from huaweicloudsdkocr.v1.model.recognize_quota_invoice_response import RecognizeQuotaInvoiceResponse
from huaweicloudsdkocr.v1.model.recognize_taxi_invoice_request import RecognizeTaxiInvoiceRequest
from huaweicloudsdkocr.v1.model.recognize_taxi_invoice_response import RecognizeTaxiInvoiceResponse
from huaweicloudsdkocr.v1.model.recognize_toll_invoice_request import RecognizeTollInvoiceRequest
from huaweicloudsdkocr.v1.model.recognize_toll_invoice_response import RecognizeTollInvoiceResponse
from huaweicloudsdkocr.v1.model.recognize_train_ticket_request import RecognizeTrainTicketRequest
from huaweicloudsdkocr.v1.model.recognize_train_ticket_response import RecognizeTrainTicketResponse
from huaweicloudsdkocr.v1.model.recognize_transportation_license_request import RecognizeTransportationLicenseRequest
from huaweicloudsdkocr.v1.model.recognize_transportation_license_response import RecognizeTransportationLicenseResponse
from huaweicloudsdkocr.v1.model.recognize_vin_request import RecognizeVINRequest
from huaweicloudsdkocr.v1.model.recognize_vin_response import RecognizeVINResponse
from huaweicloudsdkocr.v1.model.recognize_vat_invoice_items_response import RecognizeVatInvoiceItemsResponse
from huaweicloudsdkocr.v1.model.recognize_vat_invoice_request import RecognizeVatInvoiceRequest
from huaweicloudsdkocr.v1.model.recognize_vat_invoice_request_body import RecognizeVatInvoiceRequestBody
from huaweicloudsdkocr.v1.model.recognize_vat_invoice_response import RecognizeVatInvoiceResponse
from huaweicloudsdkocr.v1.model.recognize_vat_invoice_result_response import RecognizeVatInvoiceResultResponse
from huaweicloudsdkocr.v1.model.recognize_vehicle_license_request import RecognizeVehicleLicenseRequest
from huaweicloudsdkocr.v1.model.recognize_vehicle_license_request_body import RecognizeVehicleLicenseRequestBody
from huaweicloudsdkocr.v1.model.recognize_vehicle_license_response import RecognizeVehicleLicenseResponse
from huaweicloudsdkocr.v1.model.recognize_vehicle_license_result_response import RecognizeVehicleLicenseResultResponse
from huaweicloudsdkocr.v1.model.recognize_web_image_request import RecognizeWebImageRequest
from huaweicloudsdkocr.v1.model.recognize_web_image_response import RecognizeWebImageResponse
from huaweicloudsdkocr.v1.model.taxi_invoice_req import TaxiInvoiceReq
from huaweicloudsdkocr.v1.model.taxi_invoice_result_body import TaxiInvoiceResultBody
from huaweicloudsdkocr.v1.model.toll_invoice_req import TollInvoiceReq
from huaweicloudsdkocr.v1.model.toll_invoice_result_body import TollInvoiceResultBody
from huaweicloudsdkocr.v1.model.train_ticket_req import TrainTicketReq
from huaweicloudsdkocr.v1.model.train_ticket_result_body import TrainTicketResultBody
from huaweicloudsdkocr.v1.model.transportation_license_req import TransportationLicenseReq
from huaweicloudsdkocr.v1.model.transportation_license_result_body import TransportationLicenseResultBody
from huaweicloudsdkocr.v1.model.vin_req import VINReq
from huaweicloudsdkocr.v1.model.vin_response_body_item import VINResponseBodyItem
from huaweicloudsdkocr.v1.model.web_image_items_response import WebImageItemsResponse
from huaweicloudsdkocr.v1.model.web_image_req import WebImageReq
from huaweicloudsdkocr.v1.model.web_image_response_body_item import WebImageResponseBodyItem

