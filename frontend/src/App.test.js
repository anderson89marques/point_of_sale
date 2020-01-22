import React from 'react';
import ShallowRenderer from 'react-test-renderer/shallow';
import App from './App';
import OrderItemInfo from './components/OrderItemInfo';
import OrderItemForm from './components/OrderItemForm';
import ListOrderItens from './components/ListOrderItens';
import Header from './components/Header';
import SaleData from './components/SaleData';
import OrderModal from './components/OrderModal';
import Pos from  './pages/pos';


test('App component returns a div', () => {
  const renderer = new ShallowRenderer();
  renderer.render(<App />);
  const result = renderer.getRenderOutput();
  expect(result.type).toBe('div');
});

test('App component returns a correct children', () => {
  const renderer = new ShallowRenderer();
  renderer.render(<App />);
  const result = renderer.getRenderOutput();
  expect(result.props.children).toEqual([
    <Header />,
    <Pos />]);
});

test('Pos component returns a container class', () => {
  const renderer = new ShallowRenderer();
  renderer.render(<Pos />);
  const result = renderer.getRenderOutput();
  expect(result.type.displayName).toEqual('Container');
});

test('OrderItemInfo component returns a section', () => {
  const renderer = new ShallowRenderer();
  renderer.render(<OrderItemInfo />);
  const result = renderer.getRenderOutput();
  expect(result.type).toBe('section');
  });


test('OrderItemInfo component returns correct children', () => {
  const renderer = new ShallowRenderer();
  renderer.render(<OrderItemInfo />);
  const result = renderer.getRenderOutput();
  expect(result.props.children).toEqual([
    <OrderItemForm />,
    <ListOrderItens />]);
});