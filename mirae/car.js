import * as THREE from 'three';

// Generic unbranded sedan built from extruded side profiles. Front faces -z, right side is +x.
const FA = -1.42, RA = 1.4, WR = 0.34, ARCH = 0.46;

function sideExtrude(shape, depth, thick, size, mat) {
  const g = new THREE.ExtrudeGeometry(shape, { depth, bevelEnabled: true, bevelThickness: thick, bevelSize: size, bevelSegments: 8, curveSegments: 36 });
  g.translate(0, 0, -depth / 2);
  g.rotateY(-Math.PI / 2);
  g.computeVertexNormals();
  return new THREE.Mesh(g, mat);
}

function box(w, h, d, mat, x, y, z) {
  const m = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), mat);
  m.position.set(x, y, z);
  return m;
}

function wheel(side, rubber, alloy, dark) {
  const g = new THREE.Group();
  const tire = new THREE.Mesh(new THREE.CylinderGeometry(WR, WR, 0.24, 48), rubber);
  tire.rotation.z = Math.PI / 2;
  const wall = new THREE.Mesh(new THREE.TorusGeometry(WR - 0.03, 0.035, 12, 48), rubber);
  wall.rotation.y = Math.PI / 2;
  wall.position.x = 0.1 * side;
  const disc = new THREE.Mesh(new THREE.CylinderGeometry(0.235, 0.235, 0.245, 40), dark);
  disc.rotation.z = Math.PI / 2;
  const lip = new THREE.Mesh(new THREE.TorusGeometry(0.235, 0.018, 10, 48), alloy);
  lip.rotation.y = Math.PI / 2;
  lip.position.x = 0.124 * side;
  const hub = new THREE.Mesh(new THREE.CylinderGeometry(0.06, 0.06, 0.26, 20), alloy);
  hub.rotation.z = Math.PI / 2;
  g.add(tire, wall, disc, lip, hub);
  for (let i = 0; i < 5; i++) {
    const a = (i / 5) * Math.PI * 2;
    const spoke = box(0.02, 0.19, 0.075, alloy, 0.128 * side, Math.cos(a) * 0.12, Math.sin(a) * 0.12);
    spoke.rotation.x = a;
    g.add(spoke);
  }
  return g;
}

export function buildCar(paint) {
  const car = new THREE.Group();
  const trim = new THREE.MeshStandardMaterial({ color: 0x14161a, roughness: 0.55, metalness: 0.2 });
  const glass = new THREE.MeshPhysicalMaterial({ color: 0x0b0e13, metalness: 0.3, roughness: 0.05, clearcoat: 1, clearcoatRoughness: 0.02 });
  const rubber = new THREE.MeshStandardMaterial({ color: 0x131313, roughness: 0.92 });
  const alloy = new THREE.MeshStandardMaterial({ color: 0xcfd4da, metalness: 1, roughness: 0.28 });
  const dark = new THREE.MeshStandardMaterial({ color: 0x23272c, metalness: 0.5, roughness: 0.5 });
  const head = new THREE.MeshStandardMaterial({ color: 0xffffff, emissive: 0xe8f0ff, emissiveIntensity: 1.3 });
  const tail = new THREE.MeshStandardMaterial({ color: 0x3a0000, emissive: 0xff2020, emissiveIntensity: 0.9 });
  const plate = new THREE.MeshStandardMaterial({ color: 0xe9ecef, roughness: 0.5 });

  const s = new THREE.Shape();
  s.moveTo(-2.2, 0.22);
  s.lineTo(FA - ARCH, 0.22);
  s.lineTo(FA - ARCH, WR);
  s.absarc(FA, WR, ARCH, Math.PI, 0, true);
  s.lineTo(FA + ARCH, 0.22);
  s.lineTo(RA - ARCH, 0.22);
  s.lineTo(RA - ARCH, WR);
  s.absarc(RA, WR, ARCH, Math.PI, 0, true);
  s.lineTo(RA + ARCH, 0.22);
  s.lineTo(2.18, 0.22);
  s.quadraticCurveTo(2.33, 0.26, 2.32, 0.5);
  s.quadraticCurveTo(2.31, 0.78, 2.16, 0.84);
  s.lineTo(1.3, 0.92);
  s.lineTo(-1.05, 0.86);
  s.quadraticCurveTo(-1.95, 0.8, -2.2, 0.68);
  s.quadraticCurveTo(-2.34, 0.6, -2.33, 0.42);
  s.quadraticCurveTo(-2.32, 0.24, -2.2, 0.22);
  const body = sideExtrude(s, 1.72, 0.07, 0.05, paint);
  body.name = 'body';

  const c = new THREE.Shape();
  c.moveTo(-1.05, 0.84);
  c.quadraticCurveTo(-0.62, 1.2, -0.3, 1.4);
  c.quadraticCurveTo(0.2, 1.46, 0.62, 1.4);
  c.quadraticCurveTo(1.0, 1.24, 1.32, 0.9);
  c.lineTo(1.32, 0.84);
  c.lineTo(-1.05, 0.84);
  const cabin = sideExtrude(c, 1.46, 0.08, 0.04, glass);

  const r = new THREE.Shape();
  r.moveTo(-0.3, 1.4);
  r.quadraticCurveTo(0.2, 1.46, 0.62, 1.4);
  r.lineTo(0.6, 1.37);
  r.quadraticCurveTo(0.2, 1.425, -0.28, 1.37);
  r.lineTo(-0.3, 1.4);
  const roof = sideExtrude(r, 1.46, 0.085, 0.045, paint);

  car.add(body, cabin, roof, box(1.64, 0.5, 0.07, trim, 0, 1.15, 0.2));

  // front
  car.add(box(1.1, 0.16, 0.12, trim, 0, 0.4, -2.33));
  car.add(box(0.5, 0.11, 0.02, plate, 0, 0.44, -2.4));
  for (const x of [-0.56, 0.56]) car.add(box(0.44, 0.05, 0.1, head, x, 0.66, -2.25));
  car.add(box(1.2, 0.018, 0.06, head, 0, 0.705, -2.24));
  // rear
  car.add(box(1.55, 0.05, 0.1, tail, 0, 0.74, 2.32));
  car.add(box(0.5, 0.11, 0.02, plate, 0, 0.5, 2.375));

  for (const side of [-1, 1]) {
    const m = new THREE.Mesh(new THREE.SphereGeometry(0.075, 20, 14), paint);
    m.scale.set(1.1, 0.75, 1.5);
    m.position.set(1.02 * side, 0.97, -0.98);
    car.add(m, box(0.1, 0.022, 0.04, trim, 0.94 * side, 0.93, -0.95));
    for (const z of [-0.3, 0.72]) car.add(box(0.015, 0.03, 0.15, alloy, 0.935 * side, 0.8, z));
    for (const [z, y0, y1] of [[FA + ARCH, 0.3, 0.86], [0.2, 0.26, 0.9], [RA - ARCH, 0.8, 0.92]]) {
      car.add(box(0.006, y1 - y0, 0.012, trim, 0.933 * side, (y0 + y1) / 2, z));
    }
    car.add(box(0.01, 0.05, (RA - ARCH) - (FA + ARCH), trim, 0.932 * side, 0.26, (FA + RA) / 2));
  }

  for (const [x, z] of [[-0.8, FA], [0.8, FA], [-0.8, RA], [0.8, RA]]) {
    const w = wheel(Math.sign(x), rubber, alloy, dark);
    w.position.set(x, WR, z);
    car.add(w);
  }

  const shadow = new THREE.Mesh(new THREE.PlaneGeometry(2.6, 5.4), new THREE.MeshBasicMaterial({ map: shadowTexture(), transparent: true, depthWrite: false, toneMapped: false }));
  shadow.rotation.x = -Math.PI / 2;
  shadow.position.y = 0.004;
  shadow.renderOrder = 2;
  car.add(shadow);
  return car;
}

function shadowTexture() {
  const cv = document.createElement('canvas');
  cv.width = 128; cv.height = 256;
  const g = cv.getContext('2d');
  const grad = g.createRadialGradient(64, 128, 10, 64, 128, 124);
  grad.addColorStop(0, 'rgba(0,0,0,.85)');
  grad.addColorStop(0.55, 'rgba(0,0,0,.55)');
  grad.addColorStop(1, 'rgba(0,0,0,0)');
  g.setTransform(1, 0, 0, 1, 0, 0);
  g.scale(1, 1);
  g.fillStyle = grad;
  g.beginPath();
  g.ellipse(64, 128, 60, 124, 0, 0, Math.PI * 2);
  g.fill();
  const t = new THREE.CanvasTexture(cv);
  t.colorSpace = THREE.SRGBColorSpace;
  return t;
}

// Scratches and a dent on the right front door, used to show accident damage.
export const DAMAGE_POS = new THREE.Vector3(0.935, 0.58, -0.4);

export function buildDamage() {
  const cv = document.createElement('canvas');
  cv.width = 512; cv.height = 384;
  const g = cv.getContext('2d');
  const dent = g.createRadialGradient(230, 200, 8, 250, 190, 170);
  dent.addColorStop(0, 'rgba(0,0,0,.55)');
  dent.addColorStop(0.45, 'rgba(0,0,0,.28)');
  dent.addColorStop(0.75, 'rgba(255,255,255,.10)');
  dent.addColorStop(1, 'rgba(255,255,255,0)');
  g.fillStyle = dent;
  g.fillRect(0, 0, 512, 384);
  let seed = 7;
  const rnd = () => ((seed = (seed * 16807) % 2147483647) / 2147483647);
  for (let i = 0; i < 16; i++) {
    const x0 = 70 + rnd() * 150, y0 = 140 + rnd() * 110;
    const len = 90 + rnd() * 230, ang = -0.16 + rnd() * 0.2;
    g.strokeStyle = i % 5 === 0 ? 'rgba(245,247,250,.9)' : `rgba(${170 + rnd() * 50 | 0},${175 + rnd() * 50 | 0},${182 + rnd() * 50 | 0},${0.35 + rnd() * 0.4})`;
    g.lineWidth = i % 5 === 0 ? 2.5 + rnd() * 2 : 0.8 + rnd() * 1.6;
    g.beginPath();
    g.moveTo(x0, y0);
    let x = x0, y = y0;
    for (let k = 0; k < 8; k++) { x += (len / 8) * Math.cos(ang); y += (len / 8) * Math.sin(ang) + (rnd() - 0.5) * 6; g.lineTo(x, y); }
    g.stroke();
  }
  for (let i = 0; i < 9; i++) {
    g.fillStyle = i % 3 ? 'rgba(150,155,160,.85)' : 'rgba(235,238,241,.9)';
    g.beginPath();
    g.ellipse(160 + rnd() * 200, 160 + rnd() * 90, 2 + rnd() * 6, 1.5 + rnd() * 3.5, rnd() * 3, 0, Math.PI * 2);
    g.fill();
  }
  const t = new THREE.CanvasTexture(cv);
  t.colorSpace = THREE.SRGBColorSpace;
  const mat = new THREE.MeshStandardMaterial({ map: t, transparent: true, roughness: 0.6, depthWrite: false, polygonOffset: true, polygonOffsetFactor: -4 });
  const m = new THREE.Mesh(new THREE.PlaneGeometry(0.72, 0.54), mat);
  m.position.copy(DAMAGE_POS);
  m.rotation.y = Math.PI / 2;
  return m;
}
