class Element {
	constructor(name) {
		this.element = document.createElement(name)
	};

	set(config) {
		for (let i in config) {
			this.element.setAttribute(i, config[i])
		}
	}
};

$ = name => new Element(name);


class csi {
	constructor(config) {
		this.svg = $("svg");

		this.svg.set({
			...config,
			xmlns: "http://www.w3.org/2000/svg"
		})

	};
	draw(config) {
		for (let i of config) {
			let element = $(i.name);

			element.set(i.config);
			this.svg.element.appendChild(element.element);
		};
		return this.svg
	}
}