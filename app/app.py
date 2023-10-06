from ipaddress import IPv4Address, IPv4Interface, IPv4Network

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

	if request.method == 'POST':
		ip_info = {}
		net_info = {}
		details = {}
		operation = request.form.get("select")
		input_text = request.form['inputText']
		print("Text that was entered:", input_text)
		print("radio selected:", operation)
		if operation == None:
			return render_template('base.html', no_selection=True)
		
		if input_text == "":
			return render_template('base.html', no_text=True)
		
		if operation == 'addressSelected':
			try:
				address = IPv4Address(input_text)
				ip_info['loopback_ip'] = address.is_loopback
				ip_info['multicast_ip'] = address.is_multicast
				ip_info['private_ip'] = address.is_private
				ip_info['reserved_ip'] = address.is_reserved
				return render_template('base.html', ip_info=ip_info, input_text=input_text)

			except ValueError:
				print("This is not a valid IP address!")
				return render_template('base.html', invalid_text=True)

		elif operation == 'netSelected':
			try:
				net = IPv4Network(input_text)
				net_info['num_addresses'] = net.num_addresses-2
				net_info['prefix_len'] = net.prefixlen
				net_info['netmask'] = net.netmask
				net_info['net_address'] = net.network_address
				net_info['broadcast'] = net.broadcast_address
				return render_template('base.html', net_info=net_info, input_text=input_text)
			
			except ValueError:
				print("This is not a valid subnet!")
				return render_template('base.html', invalid_text=True)
					
		elif operation == 'detailSelected':
			try:
				interface = IPv4Interface(input_text)
				details['ip_addr'] = interface.ip.exploded
				details['mask'] = interface.netmask
				details['net_addr'] = interface.network.network_address
				details['broadcast'] = interface.network.broadcast_address
				details['first_host'] = interface.network.network_address+1
				details['last_host'] = interface.network.broadcast_address-1
				return render_template('base.html', details=details, input_text=input_text)

			except ValueError:
				print("This is not a valid subnet!")
				return render_template('base.html', invalid_text=True)


	return render_template('base.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=10000)
