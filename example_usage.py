from client import ProptechLeasingMultimodalInquirySchedulerAgentClient

def main():
    client = ProptechLeasingMultimodalInquirySchedulerAgentClient()
    res = client.schedule_property_tour_and_lease_qualification('Alex Rivera', 'WHATSAPP_AI_AGENT', 'Penthouse 1204')
    print('Inquiry ID: ' + res['lease_inquiry_id'] + ' for ' + res['prospective_tenant'])
    print('Smart Lock Tour: ' + res['self_guided_smart_lock_tour_booked_time'] + ' (Qualified: ' + str(res['credit_income_prequalification_passed']) + ')')
    print('Yardi Synced: ' + str(res['property_management_yardi_realpage_synced']) + ' | Conversion Lift: +' + str(res['leasing_conversion_rate_lift_pct']) + '%')

if __name__ == '__main__':
    main()
