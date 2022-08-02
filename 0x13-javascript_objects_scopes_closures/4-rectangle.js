#!/usr/bin/node
module.exports = class Rectangle {
	constructor(w, h) {
		if (w > 0 && h > 0)
		{
			this.width = w;
			this.height = h;
		}
	}
	// print a rectangle using X character
	print() {
		for (let i = 0; i < this.height; i++) {
			for (let j = 0; j < this.width; j++) {
				process.stdout.write('X');
			}
			console.log();
		}
	}

	// rotate the values of width and height
	rotate() {
		let tmp = this.width;
		this.width = this.height;
		this.height = tmp;
	}

	// double the value of width and height
	double() {
		this.width = this.width * 2;
		this.height = this.height * 2;
	}
}
