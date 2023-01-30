build:
	docker build -t jublia .

run: build
	docker run --name email_app -d -p 4000:4000 --network email_app jublia
